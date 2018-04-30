import React from 'react';
import PropTypes from 'prop-types';

import BaseBadge from 'app/components/idBadge/baseBadge';
import SentryTypes from 'app/proptypes';
import SlugOverflow from 'app/components/idBadge/slugOverflow';

export default class ProjectBadge extends React.Component {
  static propTypes = {
    ...BaseBadge.propTypes,
    project: SentryTypes.Project.isRequired,
    avatarSize: PropTypes.number,
    hideAvatar: PropTypes.bool,
  };

  static defaultProps = {
    hideAvatar: true,
  };

  render() {
    let {project} = this.props;

    return (
      <BaseBadge
        displayName={<SlugOverflow>{project.slug}</SlugOverflow>}
        {...this.props}
      />
    );
  }
}