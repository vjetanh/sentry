import React from 'react';
import styled from 'react-emotion';
import moment from 'moment';

import {tct} from 'app/locale';
import SentryTypes from 'app/proptypes';
import space from '../../styles/space';
import InlineSvg from '../inlineSvg';
import {slideInRight} from '../../styles/animations';

const BACKFILL_DATE = '2018-05-01';

export default class BackfillNotice extends React.Component {
  static propTypes = {
    project: SentryTypes.Project,
  };

  render() {
    const shouldDisplayWarning = moment(BACKFILL_DATE).isAfter(
      moment(this.props.project.dateCreated)
    );

    return (
      shouldDisplayWarning && (
        <StyledCallout>
          <InfoIcon src="icon-circle-info" />
          {tct(
            `You can now filter by environment!
          Data before [backfillDate] may be temporarily unavailable.`,
            {
              backfillDate: moment(BACKFILL_DATE).format('MMM d'),
            }
          )}
          <CloseButton src="icon-close-lg" />
        </StyledCallout>
      )
    );
  }
}

const StyledCallout = styled.div`
  font-size: ${p => p.theme.fontSizeSmall};
  color: ${p => p.theme.textColor};
  background-color: ${p => p.theme.alert.warning.background};
  border-radius: ${p => p.theme.borderRadius};
  animation: 0.5s ${slideInRight};
  width: 305px;
  padding: ${space(1)};
  position: absolute;
  right: calc(100% + ${space(2)});
  display: flex;
  align-items: center;
  &:before {
    content: '';
    border-style: solid;
    border-width: ${space(1)} 0 ${space(1)} ${space(1)};
    border-color: transparent transparent transparent
      ${p => p.theme.alert.warning.background};
    position: absolute;
    left: 100%;
    top: 50%;
    transform: translateY(-50%);
  }
`;

const InfoIcon = styled(InlineSvg)`
  fill: ${p => p.theme.textColor};
  width: 20px;
  height: 20px;
  margin-right: ${space(1)};
  flex-shrink: 0;
`;

const CloseButton = styled(InlineSvg)`
  stroke: ${p => p.theme.gray4};
  width: 16px;
  height: 16px;
  margin: 0 ${space(0.5)} 0 ${space(1)};
`;
